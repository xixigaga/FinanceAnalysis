# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.contract.common import Region, Provider
from zvt.domain.quotes import BlockKdataCommon

KdataBase = declarative_base()


class Block1dKdata(KdataBase, BlockKdataCommon):
    __tablename__ = 'block_1d_kdata'


register_schema(regions=[Region.CHN, Region.US], 
                providers={Region.CHN: [Provider.EastMoney], 
                           Region.US: [Provider.Default]}, 
                db_name='block_1d_kdata', schema_base=KdataBase)

__all__ = ['Block1dKdata']
