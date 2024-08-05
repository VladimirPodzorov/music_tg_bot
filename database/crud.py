from typing import Dict, List

from database.models import Band, Album, Song, session


def insert_value(data: Dict):
    is_band = session.query(Band.id).filter(Band.name == data["band"]).one_or_none()
    if is_band:
        is_album = (
            session.query(Album.id).filter(Album.name == data["album"]).one_or_none()
        )
        if is_album:
            song = Song(
                name=data["song"],
                tg_id=data["audio"],
                band_id=is_band.id,
                album_id=is_album.id,
            )
            session.add(song)
            session.commit()
        album = Album(name=data["album"], year=data["year"], band_id=is_band.id)
        session.add(album)
        song = Song(
            name=data["song"],
            tg_id=data["audio"],
            band_id=is_band.id,
            album_id=album.id,
        )
        session.add(song)
        session.commit()
    else:
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


def get_artist(artist_name: str) -> List | str:
    # Нужно доработать!!!
    result = session.query(Band).filter(Band.name == artist_name).one_or_none()
    if result:
        return list(album.name for album in result.album)
    return "foo bar"
