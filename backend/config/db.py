from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3307/test"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)

# Crear el local session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base
Base = declarative_base()

# Dependencia de la base de datos para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
