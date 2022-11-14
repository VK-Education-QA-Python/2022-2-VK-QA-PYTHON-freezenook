from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalRequests(Base):
    __tablename__ = '1total_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    count = Column(Integer, nullable=False, primary_key=True)

    def __repr__(self):
        return f"{self.count}"


class TotalRequestsByType(Base):
    __tablename__ = '2total_requests_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    req_type = Column(String(300), nullable=False, primary_key=True)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"('{self.req_type}', {self.count})"


class Top10Requests(Base):
    __tablename__ = '3top10_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"('{self.url}', {self.count})"


class Top5Large4XX(Base):
    __tablename__ = '4top5_4xx_largest_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    error = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(30), nullable=False)

    def __repr__(self):
        return f"['{self.url}', '{self.error}', '{self.size}', '{self.ip}']"


class Top5w5XX(Base):
    __tablename__ = '5top5_5xx_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30), nullable=False)
    requests_number = Column(Integer, nullable=False)

    def __repr__(self):
        return f"('{self.ip}', {self.requests_number})"
