import 'package:flutter/material.dart';
import 'package:flutter_application_3/data/my_character.dart';
import 'package:flutter_application_3/models/character.dart';
import 'package:flutter_application_3/widgetes/list_item.dart';
import 'package:google_fonts/google_fonts.dart';

/*
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
} */

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    Character character = getMyCharacter();

    var scaffold = Scaffold(
      appBar: AppBar(
        title: const Text(
          "Meu Grande Personagem",
          style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
        ),
        backgroundColor: Colors.orange[900],
        centerTitle: true,
        shadowColor: Colors.black,
        elevation: 7,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          print("Click Realizado");
        },
        backgroundColor: Colors.orange[900],
        child: Icon(Icons.add, color: Colors.white),
      ),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: SingleChildScrollView(
          child: Column(
            children: [
              Center(child: Image.network(character.urlImage!, width: 300)),
              Text(
                character.name,
                style: GoogleFonts.seaweedScript(
                  fontSize: 64,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                "Por ${character.Player}, criar em ${character.createdAT.toString().substring(0, 10)}",
                style: TextStyle(fontStyle: FontStyle.italic),
              ),
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 16.0),
                child: const Divider(),
              ),
              ListItem(title: "Nível:", value: character.level.toString()),
              ListItem(
                title: "Vida:",
                value: "${character.hitPoints}/${character.level * 11}",
              ),
              ListItem(
                title: "Mana:",
                value: "${character.manaPoints}/${character.level * 2}",
              ),
              ListItem(
                title: "Vivo?:",
                value: (character.isAlive) ? "❤️" : "💀",
              ),
            ],
          ),
        ),
      ),
    );
    return scaffold;
  }
}
