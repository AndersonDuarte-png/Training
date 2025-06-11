class Character {
  String name;
  int level;
  double hitPoints;
  double manaPoints;
  bool isAlive;
  List<String> ListAllies;

  // about player

  String Player;
  DateTime createdAT;

  // Meta information

  String? urlImage;

  Character({
    required this.name,
    required this.level,
    required this.hitPoints,
    required this.isAlive,
    required this.createdAT,
    required this.manaPoints,
    required this.ListAllies,
    required this.Player,
    this.urlImage,
  });
}
