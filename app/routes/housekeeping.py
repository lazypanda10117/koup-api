from app import app
from app.db import db
import app.utils.datetime as datetime
import app.utils.generic as generic
import app.utils.graphqlUtil as gqlUtil
from app.models.model_room import ModelRoom
from app.models.model_player import ModelPlayer


@app.route("/housekeeping/purge/<idle_min>", methods=["GET"])
def purge_idle_rooms(idle_min):
    if idle_min.isdigit():
        idle_min = int(idle_min)

        to_purge = db.session.query(ModelRoom).filter(
            ModelRoom.last_update < datetime.time_back(idle_min)
        )
        num_purged = to_purge.count()
        for purge in to_purge.all():
            for player in purge.players:
                db.session.delete(player)
        db.session.commit()

        purge_req = ModelRoom.__table__.delete().where(
            ModelRoom.last_update < datetime.time_back(idle_min)
        )
        try:
            db.session.execute(purge_req)
            db.session.commit()
        except:
            db.session.rollback()
            print("Failed to delete expired rooms")
            raise

    elif isinstance(idle_min, str) and idle_min == "dynamic":
        num_purged = 0
        all_rooms = db.session.query(ModelRoom).all()
        for room in all_rooms:
            if room.last_update < datetime.time_back(room.max_idle_time):
                for player in room.players:
                    player_data = gqlUtil.input_to_dictionary(gqlUtil.serialize(player))
                    generic.delete_object(ModelPlayer, player_data['id'])
                generic.delete_object(ModelRoom, dict(id=room.id))
                num_purged += 1
    else:
        return "Stop Messing Around :["

    return "Purged " + str(num_purged) + " expired room(s)."
