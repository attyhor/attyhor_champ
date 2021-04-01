from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, or_
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

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    points = Column(Integer, nullable=False, default=0)
    ACTIVE = Column(Integer, nullable=False, default=1)
    CREATEDON = Column(String, nullable=False, default=datetime.datetime.now)
    UPDATEON = Column(String, onupdate=datetime.datetime.now)

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    round = Column(Integer)
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

class Season(Base):
    __tablename__ = "seasons"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class League(Base):
    __tablename__ = "leagues"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    competition_id = Column(ForeignKey("competition.id"), nullable=False)
    rounds = Column(Integer, nullable=False)
    win_points = Column(Integer, nullable=False)
    draw_points = Column(Integer, nullable=False)
    lost_points = Column(Integer, nullable=False)
    teams_number = Column(Integer, nullable=False)
    seasons_id = Column(ForeignKey("seasons.id"), nullable=False)

    competition_name = relationship(Competition, foreign_keys=[competition_id])
    seasons_name = relationship(Season, foreign_keys=[seasons_id])




engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

db = Session()


"""
    cursor.execute("CREATE TABLE IF NOT EXISTS team (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, league_id INT(11) NOT NULL,
    CONSTRAINT FOREIGN KEY (league_id) REFERENCES league (id) ON DELETE CASCADE ON UPDATE RESTRICT, team_name VARCHAR(255)) ENGINE=InnoDB")
    cursor.execute("CREATE TABLE IF NOT EXISTS `game` (`id` INT(11) NOT NULL AUTO_INCREMENT, `league_id` INT(11) NOT NULL,
    `game_type_id` INT(11) NOT NULL, `home_team_id` INT(11) NOT NULL, `visiting_team_id` INT(11) NOT NULL, `round_of_game` INT(11) NOT NULL,
    `date_of_game` DATE, `home_team_score` INT(11) NOT NULL, `visitor_team_score` INT(11) NOT NULL, `result_of_game` VARCHAR(1) NOT NULL,
    PRIMARY KEY (`id`) USING BTREE, INDEX `league_id` (`league_id`) USING BTREE, INDEX `game_type_id_ibfk_1` (`game_type_id`) USING BTREE,
    CONSTRAINT `game_type_id_ibfk_1` FOREIGN KEY (`game_type_id`) REFERENCES `league_manager`.`game_type` (`id`) ON UPDATE RESTRICT ON DELETE CASCADE, CONSTRAINT `league_id_ibfk_1` FOREIGN KEY (`league_id`) REFERENCES `league_manager`.`league` (`id`) ON UPDATE RESTRICT ON DELETE CASCADE, CONSTRAINT `home_team_id_ibfk_1` FOREIGN KEY (`home_team_id`) REFERENCES `league_manager`.`team` (`id`) ON UPDATE RESTRICT ON DELETE CASCADE, CONSTRAINT `visiting_team_id_ibfk_1` FOREIGN KEY (`visiting_team_id`) REFERENCES `league_manager`.`team` (`id`) ON UPDATE RESTRICT ON DELETE CASCADE  )  COLLATE='utf8_general_ci'  ENGINE=InnoDB  ;")
"""