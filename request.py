from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

def search_contacts_by_surname(fullname):
    engine = create_engine("mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-RCOTVQJ;DATABASE=contacts;UID=cont;PWD=contact")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Contact).filter(Contact.fullname.like(f"%{fullname}%"))
    contacts = query.all()
    session.close()
    return contacts

def search_contacts_by_phone(phone):
    engine = create_engine("mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-RCOTVQJ;DATABASE=contacts;UID=cont;PWD=contact")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Contact).filter(Contact.phonenum == phone)
    contacts = query.all()
    session.close()
    return contacts

def search_contacts_by_passport(passport):
    engine = create_engine("mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-RCOTVQJ;DATABASE=contacts;UID=cont;PWD=contact")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Contact).filter(Contact.passp == passport)
    contacts = query.all()
    session.close()
    return contacts

# Определение базового класса для моделей
Base = declarative_base()

# Определение модели данных
class Contact(Base):
    __tablename__ = 'tabl'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    inn = Column(String)
    gender = Column(String)
    birthdate = Column(String)
    phonenum = Column(String)
    affiliation = Column(String)
    passp = Column(String)
    snils = Column(String)
    city = Column(String)

def search_contacts_by_surname(fullname):
    # Создание подключения к базе данных
    engine = create_engine("mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-RCOTVQJ;DATABASE=contacts;UID=cont;PWD=contact")
    
    # Создание сессии
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Формирование запроса с поиском по вхождению фамилии
    query = session.query(Contact).filter(Contact.fullname.like(f"%{fullname}%"))
    print("Текст запроса:", query)
    
    # Выполнение запроса
    contacts = query.all()
    print("Результаты запроса:", contacts)

    # Закрыть сессию после использования
    session.close()

    return contacts
