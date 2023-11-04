#!/usr/bin/env python3
"""
"""
# install library
from sqlalchemy import Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# standard library
from datetime import datetime, timezone
import json

# project module
from ..mysql import profil_db as db


# user profil

class Profil(db.Model):

    # personal informations
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)
    genre: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)
    job: Mapped[str] = mapped_column(String) # ton travail - specialité
    about: Mapped[str] = mapped_column(Text) # breve description

    # sensible informations
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    
    # social informations
    picture: Mapped[str] = mapped_column(String) # photo
    github: Mapped[str] = mapped_column(String, unique=True)
    gitlab: Mapped[str] = mapped_column(String, unique=True)
    twitter: Mapped[str] = mapped_column(String, unique=True)
    linkedin: Mapped[str] = mapped_column(String, unique=True)
    website: Mapped[str] = mapped_column(String, unique=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    # relationship
    experiences = relationship('Experience')
    formations = relationship('Formation')
    languages = relationship('Language')
    abonnements = relationship('Abonnement')


    @property
    def datadict(self):

        return {
            'id': self.id,
            'create_at': self.create_at,
            'update_at': self.update_at,
            'username': self.username,
            'firstname': self.firstname if self.firstname else '',
            'lastname': self.lastname if self.lastname else '',
            'genre': self.genre if self.genre else '',
            'phone': self.phone if self.phone else '',
            'country': self.country if self.country else '',
            'job': self.job if self.job else '',
            'about': self.about if self.about else '',
            'email': self.email,
            'picture': self.picture if self.picture else '',
            'github': self.github if self.github else '',
            'gitlab': self.gitlab if self.gitlab else '',
            'twitter': self.twitter if self.twitter else '',
            'linkedin': self.linkedin if self.linkedin else '',
            'website': self.website if self.website else '',
            'experiences': {
                    
            },
            'formation': {

            },
            'languages': {

            },
        }
    
    @property
    def json(self):
        return json.dumps(self.datadict)

    

# user skills informations

class Experience(db.Model):

    profil_id: Mapped[str] = mapped_column(String, ForeignKey(Profil.id, ondelete='CASCADE'))
    profil = relationship('Profil', back_populates='experiences', foreign_keys=[profil_id])

    title: Mapped[str] = mapped_column(String, nullable=False)
    start: Mapped[datetime] = mapped_column(String, default=datetime.now(tz=timezone))
    end: Mapped[datetime] = mapped_column(String, default=datetime.now(tz=timezone))
    description: Mapped[str] = mapped_column(Text)

    @property
    def datadict(self):
        return {
            'title': self.title,
            'start': self.start,
            'end': self.end if self.end else datetime.now(tz=timezone.utc),
            'description': self.description if self.description else ''
        }

    @property
    def json(self):
        return json.dumps(self.datadict)


class Formation(db.Model):

    profil_id: Mapped[str] = mapped_column(String, ForeignKey(Profil.id, ondelete='CASCADE'))
    Profil = relationship('Profil', back_populates='formations', foreign_keys=[profil_id])

    title: Mapped[str] = mapped_column(String, nullable=False)
    start: Mapped[datetime] = mapped_column(String, default=datetime.now(tz=timezone))
    end: Mapped[datetime] = mapped_column(String, default=datetime.now(tz=timezone))
    where: Mapped[str] = mapped_column(String) # lieu
    link: Mapped[str] = mapped_column(String) # lien du diplome
    description: Mapped[str] = mapped_column(Text)

    @property
    def datadict(self):
        pass

    @property
    def json(self):
        pass


class Language(db.Model):

    profil_id: Mapped[str] = mapped_column(String, ForeignKey(Profil.id, ondelete='CASCADE'))
    Profil = relationship('Profil', back_populates='languages', foreign_keys=[profil_id])

    lang: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[str] = mapped_column(String) # année d'experience

    @property
    def datadict(self):
        pass

    @property
    def json(self):
        pass


# abonnement informations

class Abonnement(db.Model):

    profil_id: Mapped[str] = mapped_column(String, ForeignKey(Profil.id, ondelete='CASCADE'))
    Profil = relationship('Profil', back_populates='abonnements', foreign_keys=[profil_id])

    entreprise_id: Mapped[str] = mapped_column(String, ForeignKey('Entreprise.id', ondelete='CASCADE'))
    entreprise = relationship('Entreprise', back_populates='abonnements', foreign_keys=[entreprise_id])

    name: Mapped[str] = mapped_column(String, nullable=False)
    duration: Mapped[datetime] = mapped_column(DateTime) # date de fin de l'abonnement

    permissions = relationship('Permission', back_populates='abonnement')

    @property
    def datadict(self):
        pass

    @property
    def json(self):
        pass



class Permission(db.Model):

    abonnement_id: Mapped[str] = mapped_column(String, ForeignKey(Abonnement.id, ondelete='CASCADE'))
    abonnement = relationship('Abonnement', back_populates='permissions', foreign_keys=[abonnement_id])

    @property
    def datadict(self):
        pass

    @property
    def json(self):
        pass



# profil entreprise

class Entreprise(db.Model):

    company: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)
    domain: Mapped[str] = mapped_column(String)
    about: Mapped[str] = mapped_column(Text)

    # sensible informations
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)

    # social informations
    picture: Mapped[str] = mapped_column(String) # photo
    github: Mapped[str] = mapped_column(String, unique=True)
    gitlab: Mapped[str] = mapped_column(String, unique=True)
    twitter: Mapped[str] = mapped_column(String, unique=True)
    linkedin: Mapped[str] = mapped_column(String, unique=True)
    website: Mapped[str] = mapped_column(String, unique=True)

    abonnements = relationship('Abonnement')

    @property
    def datadict(self):
        pass

    @property
    def json(self):
        pass
