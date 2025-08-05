import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as f:
        config = json.load(f)

    for nickname, value in config.items():
        email = value["email"]
        bio = value["bio"]

        race_data = value.get("race")
        race = Race.objects.get_or_create(
            name=race_data["name"], description=race_data["description"])[0]

        guild_data = value.get("guild")
        if guild_data:
            description = (
                guild_data)["description"] if ("description" in
                                               guild_data) else None
            guild = Guild.objects.get_or_create(
                name=guild_data["name"], description=description)[0]
        else:
            guild = None

        if race_data["skills"]:

            for skills in race_data["skills"]:

                Skill.objects.get_or_create(name=skills["name"],
                                            bonus=skills["bonus"], race=race)
        else:
            race_data["skills"] = []

        Player.objects.create(nickname=nickname,
                              email=email, bio=bio, race=race, guild=guild)


if __name__ == "__main__":
    main()
