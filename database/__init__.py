"""
 * @author     NickyLrca   <nickylalrochhara917@gmail.com>
 * @date          2022-09-06 10:12:09
 * @projectName   Sangtei
 * Copyright @NickyLrca All rights reserved
"""
from async_pymongo import AsyncClient

from Sangtei.vars import DATABASE_NAME, DATABASE_URI

mongo = AsyncClient(DATABASE_URI)
dbname = mongo[DATABASE_NAME]
