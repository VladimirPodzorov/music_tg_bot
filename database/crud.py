from typing import Dict

from database.models import Band, Album, Song, session


def insert_value(data: Dict):
    band = Band(name=data["band"])
    session.add(band)
    session.commit()
    band_id = session.query(Band.id).filter(Band.name == data["band"]).scalar()
    album = Album(name=data["album"], year=data["year"], band_id=band_id)
    session.add(album)
    song = Song(
        name=data["song"], tg_id=data["audio"], band_id=band.id, album_id=album.id
    )
    session.add(song)
    session.commit()
