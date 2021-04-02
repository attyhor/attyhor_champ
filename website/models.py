from flask_login import UserMixin
# from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
import datetime

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True)
    password = Column(String(150))
    first_name = Column(String(150))
    last_name = Column(String(150))
    ACTIVE = Column(Integer, nullable=False, default=1)


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    points = Column(Integer, nullable=False, default=0)
    ACTIVE = Column(Integer, nullable=False, default=1)
    CREATEDON = Column(String, nullable=False, default=datetime.datetime.now)
    UPDATEON = Column(String, onupdate=datetime.datetime.now)
    ACTIVE = Column(Integer, nullable=False, default=1)


class Season(Base):
    __tablename__ = "seasons"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class League(Base):
    __tablename__ = "league"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    # competition_id = Column(ForeignKey("competition.id"), nullable=False)
    rounds = Column(Integer, nullable=False)
    win_points = Column(Integer, nullable=False)
    draw_points = Column(Integer, nullable=False)
    lost_points = Column(Integer, nullable=False)
    teams_number = Column(Integer, nullable=False)
    seasons_id = Column(ForeignKey("seasons.id"), nullable=False)
    ACTIVE = Column(Integer, nullable=False, default=1)

    # competition_name = relationship(Competition, foreign_keys=[competition_id])
    seasons_name = relationship(Season, foreign_keys=[seasons_id])


class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    round = Column(Integer)
    league_id = Column(ForeignKey("league.id"), nullable=False)
    home_id = Column(ForeignKey("teams.id"), nullable=False)
    guest_id = Column(ForeignKey("teams.id"), nullable=False)
    home_score = Column(Integer, nullable=False)
    guest_score = Column(Integer, nullable=False)
    winner = Column(Integer, nullable=False)
    date = Column(String)
    ACTIVE = Column(Integer, nullable=False, default=1)
    CREATEDON = Column(String, nullable=False, default=datetime.datetime.now)
    UPDATEON = Column(String, onupdate=datetime.datetime.now)

    home_team = relationship(Team, foreign_keys=[home_id])
    guest_team = relationship(Team, foreign_keys=[guest_id])
    league_name = relationship(League, foreign_keys=[league_id])


engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

db = Session()

# datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")
