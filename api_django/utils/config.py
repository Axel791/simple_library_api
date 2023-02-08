from dataclasses import dataclass
from environs import Env


@dataclass
class DbConfig:
    pg_host: str
    pg_port: int
    pg_user: str
    pg_password: str
    pg_name: str


@dataclass
class EmailConfig:
    email_host: str
    email_port: int
    email_host_user: str
    email_host_password: str


@dataclass
class RedisConfig:
    port: int
    host: str


@dataclass
class Config:
    db: DbConfig
    email: EmailConfig
    redis: RedisConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        db=DbConfig(
            pg_name=env.str("PG_NAME"),
            pg_user=env.str("PG_USER"),
            pg_password=env.str("PG_PASSWORD"),
            pg_host=env.str("PG_HOST"),
            pg_port=env.int("PG_PORT")
        ),
        email=EmailConfig(
            email_host=env.str("EMAIL_HOST"),
            email_port=env.int("EMAIL_PORT"),
            email_host_user=env.str("EMAIL_HOST_USER"),
            email_host_password=env.str("EMAIL_HOST_PASSWORD")
        ),
        redis=RedisConfig(
            host=env.str("REDIS_HOST"),
            port=env.int("REDIS_PORT")
        )
    )
