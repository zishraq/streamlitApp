from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, Float, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)


class MedicalStaff(Base):
    __tablename__ = 'medical_staff'

    staff_id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)


class Admission(Base):
    __tablename__ = 'admissions'

    admission_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'))
    staff_id = Column(Integer, ForeignKey('medical_staff.staff_id'))
    admission_date = Column(DateTime, nullable=False)
    discharge_date = Column(DateTime)
    patient = relationship("Patient", backref="admissions")
    staff = relationship("MedicalStaff", backref="admissions")


class LabResult(Base):
    __tablename__ = 'lab_results'

    lab_result_id = Column(Integer, primary_key=True)
    admission_id = Column(Integer, ForeignKey('admissions.admission_id'))
    test_id = Column(Integer, nullable=False)
    HR = Column(Integer)
    O2Sat = Column(Integer)
    Temp = Column(Float)
    SBP = Column(Integer)
    MAP = Column(Integer)
    DBP = Column(Integer)
    Resp = Column(Integer)
    EtCO2 = Column(Integer)
    BaseExcess = Column(Float)
    HCO3 = Column(Float)
    FiO2 = Column(Float)
    PaCO2 = Column(Float)
    SaO2 = Column(Float)
    AST = Column(Integer)
    BUN = Column(Float)
    Alkalinephos = Column(Integer)
    Calcium = Column(Float)
    Glucose = Column(Float)
    Bilirubin_total = Column(Float)
    Hgb = Column(Float)
    Platelets = Column(Float)
    SepsisLabel = Column(Integer)
    test_name = Column(String(100), nullable=False)
    result = Column(String(100), nullable=False)
    test_date = Column(Date, nullable=False)
    admission = relationship("Admission", backref="lab_results")


class Medication(Base):
    __tablename__ = 'medications'

    medication_id = Column(Integer, primary_key=True)
    admission_id = Column(Integer, ForeignKey('admissions.admission_id'))
    medication_name = Column(String(100), nullable=False)
    dosage = Column(String(50), nullable=False)
    administration_time = Column(Time, nullable=False)
    admission = relationship("Admission", backref="medications")
