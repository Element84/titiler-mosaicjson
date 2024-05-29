"""
This code was pulled from stac_pydantic:
https://github.com/stac-utils/stac-pydantic/blob/master/stac_pydantic/api/search.py
"""
from datetime import datetime as dt
from typing import Any, Dict, List, Optional, Tuple, Union, cast

from geojson_pydantic.geometries import (  # type: ignore
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
    _GeometryBase,
)
from pydantic import BaseModel, Field, TypeAdapter, validator

from titiler.mosaic.models.stac_pydantic.fields import FieldsExtension
from titiler.mosaic.models.stac_pydantic.query import Operator
from titiler.mosaic.models.stac_pydantic.shared import BBox
from titiler.mosaic.models.stac_pydantic.sort import SortExtension

Intersection = Union[
    Point,
    MultiPoint,
    LineString,
    MultiLineString,
    Polygon,
    MultiPolygon,
    GeometryCollection,
]

parse_datetime = TypeAdapter(dt).validate_json


class Search(BaseModel):
    """
    The base class for STAC API searches.

    https://github.com/radiantearth/stac-api-spec/blob/master/api-spec.md#filter-parameters-and-fields
    """

    collections: Optional[List[str]]
    ids: Optional[List[str]] = None
    bbox: Optional[BBox]
    intersects: Optional[Intersection] = None
    datetime: Optional[str]
    limit: int = 10

    @property
    def start_date(self) -> Optional[dt]:
        """
        The starting bound of a temporal search
        """
        values = (self.datetime or "").split("/")
        if len(values) == 1:
            return None
        if values[0] == ".." or values[0] == "":
            return None
        return parse_datetime(values[0])

    @property
    def end_date(self) -> Optional[dt]:
        """
        The ending bound of a temporal search
        """
        values = (self.datetime or "").split("/")
        if len(values) == 1:
            return parse_datetime(values[0])
        if values[1] == ".." or values[1] == "":
            return None
        return parse_datetime(values[1])

    @validator("intersects")
    def validate_spatial(
        cls,
        v: Intersection,
        values: Dict[str, Any],
    ) -> Intersection:
        """
        Checks whether the provided bounding box values exist
        """
        if v and values["bbox"] is not None:
            raise ValueError("intersects and bbox parameters are mutually exclusive")
        return v

    @validator("bbox")
    def validate_bbox(cls, v: BBox) -> BBox:
        """
        Checks whether the provided bounding box values are valid
        """
        if v:
            # Validate order
            if len(v) == 4:
                xmin, ymin, xmax, ymax = cast(Tuple[int, int, int, int], v)
            else:
                xmin, ymin, min_elev, xmax, ymax, max_elev = cast(
                    Tuple[int, int, int, int, int, int], v
                )
                if max_elev < min_elev:
                    raise ValueError(
                        "Maximum elevation must greater than minimum elevation"
                    )

            if xmax < xmin:
                raise ValueError(
                    "Maximum longitude must be greater than minimum longitude"
                )

            if ymax < ymin:
                raise ValueError(
                    "Maximum longitude must be greater than minimum longitude"
                )

            # Validate against WGS84
            if xmin < -180 or ymin < -90 or xmax > 180 or ymax > 90:
                raise ValueError("Bounding box must be within (-180, -90, 180, 90)")

        return v

    @validator("datetime")
    def validate_datetime(cls, v: str) -> str:
        """
        Checks whether the datetime value is valid
        """
        if "/" in v:
            values = v.split("/")
        else:
            # Single date is interpreted as end date
            values = ["..", v]

        dates = []
        for value in values:
            if value == ".." or value == "":
                dates.append("..")
                continue

            parse_datetime(value)
            dates.append(value)

        if ".." not in dates:
            if parse_datetime(dates[0]) > parse_datetime(dates[1]):
                raise ValueError(
                    "Invalid datetime range, must match format (begin_date, end_date)"
                )

        return v

    @property
    def spatial_filter(self) -> Optional[_GeometryBase]:
        """Return a geojson-pydantic object representing the spatial filter for the search request.

        Check for both because the ``bbox`` and ``intersects`` parameters are mutually exclusive.
        """
        if self.bbox:
            return Polygon.from_bounds(*self.bbox)
        if self.intersects:
            return self.intersects
        else:
            return None


class ExtendedSearch(Search):
    """
    STAC API search with extensions enabled.
    """

    field: Optional[FieldsExtension] = Field(None, alias="fields")
    query: Optional[Dict[str, Dict[Operator, Any]]] = None
    sortby: Optional[List[SortExtension]] = None