import 'package:flutter_application_3/models/character.dart';

Character getMyCharacter() {
  return Character(
    name: "Phoenix",
    level: 10,
    hitPoints: 30.5,
    isAlive: true,
    createdAT: DateTime.parse("2024-01-01"),
    manaPoints: 20.5,
    ListAllies: ["Jett", "Neon", "KJ"],
    Player: "CAFE PLAYER",
    urlImage: "https://i.imgur.com/w3br79w.jpeg",
  );
}
