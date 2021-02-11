from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session as ORMSession

from contextlib import contextmanager
from typing import ContextManager


engine = create_engine('sqlite:///chat.db', echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


@contextmanager
def session_scope() -> ContextManager[ORMSession]:
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
