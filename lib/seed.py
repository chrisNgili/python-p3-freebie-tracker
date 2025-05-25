#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    company = Company(name="Safaricom", founding_year = 1997)
    session.add(company)
    session.commit()

    dev = Dev(name = "Mike")
    session.add(dev)
    session.commit()

    freebie = company.give_freebie(dev, "Laptop", 1500 )
    session.add(freebie)

    session.commit()

    # print(freebie.printer())

    # oldest = Company.oldest_company(session)
    # print(f'The oldest company is {oldest.name} founded in {oldest.founding_year}')

    # has_laptop = dev.received_one('Laptop')
    # print(f'Did {dev.name} receive a Laptop? {has_laptop}')

    # new_dev = Dev(name='Jane Smith')
    # session.add(new_dev)
    # session.commit()
    # dev.give_away(new_dev, freebie)
    # session.commit()
    # print(freebie.printer())

