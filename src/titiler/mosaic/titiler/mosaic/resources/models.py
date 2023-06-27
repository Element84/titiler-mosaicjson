"""Titiler.mosaic Models."""

import re
from typing import List, Optional, Dict, Any

from pydantic import BaseModel, validator
from stac_pydantic.api.search import ExtendedSearch

def to_camel(snake_str: str) -> str:
    """
    Converts snake_case_string to camelCaseString
    """
    first, *others = snake_str.split("_")
    return "".join([first.lower(), *map(str.title, others)])


# Link and Links derived from models in https://github.com/stac-utils/stac-pydantic
class Link(BaseModel):
    """Link Relation"""

    href: str
    rel: str
    type: Optional[str]
    title: Optional[str]


class MosaicEntity(BaseModel):
    """Mosaic Model."""

    id: str
    links: List[Link]


rfc3339_regex_str = (
    r"^(\d\d\d\d)\-(\d\d)\-(\d\d)(T|t)"
    r"(\d\d):(\d\d):(\d\d)(\.\d+)?(Z|([-+])(\d\d):(\d\d))$"
)
rfc3339_regex = re.compile(rfc3339_regex_str)

from enum import auto
from stac_pydantic.utils import AutoValueEnum

# copied from stac_pydantic, because the neq, lte, and gte were wrong (ne, le, and ge)
class Operator(str, AutoValueEnum):
    """
    https://github.com/radiantearth/stac-api-spec/tree/master/extensions/query#query-api-extension
    """

    eq = auto()
    neq = auto()
    lt = auto()
    lte = auto()
    gt = auto()
    gte = auto()
    startsWith = auto()
    endsWith = auto()
    contains = auto()


class StacApiQueryRequestBody(ExtendedSearch):
    """Common request params for MosaicJSON CRUD operations"""

    stac_api_root: str
    asset_name: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    attribution: Optional[str] = None
    version: Optional[str] = None

    # overriding limit so we can tell if it's defined or not
    limit: Optional[int]

    max_items: Optional[int]

    # overriding query to use our Operator class rather than the broken stac_pydantic one
    query: Optional[Dict[str, Dict[Operator, Any]]]

    @validator("datetime")
    def validate_datetime(cls, v):
        """
        datetime validation
        overrides default validation due to issue https://github.com/stac-utils/stac-pydantic/issues/78
        """
        if "/" in v:
            values = v.split("/")
        else:
            # Single date is interpreted as end date
            values = ["..", v]

        dates = []
        for value in values:
            if value == "..":
                dates.append(value)
                continue
            if not rfc3339_regex.match(value):
                raise ValueError(
                    f"Invalid datetime, must match format ({rfc3339_regex_str})."
                )
            dates.append(value)

        # this should get validated by the server anyway
        # if ".." not in dates:
        #     if datetime.strptime(dates[0], DATETIME_RFC339) > datetime.strptime(
        #         dates[1], DATETIME_RFC339
        #     ):
        #         raise ValueError(
        #             "Invalid datetime range, must match format (begin_date, end_date)"
        #         )
        return v


class UrisRequestBody(BaseModel):
    """model for a source body to create a mosaicjson"""

    # option 2 - a list of files and min/max zoom
    urls: List[str]
    minzoom: Optional[int] = None
    maxzoom: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    attribution: Optional[str] = None
    version: Optional[str] = None


class TooManyResultsException(Exception):
    """exception when there are too many STAC API results to generate a mosaicjson"""

    def __init__(self, message):
        """init"""
        self.message = message


class StoreException(Exception):
    """exception when there is a problem storing the mosaicjson in the datastore"""

    def __init__(self, message):
        """init"""
        self.message = message


class UnsupportedOperationException(Exception):
    """exception for unsupported operation"""

    def __init__(self, message):
        """init"""
        self.message = message
