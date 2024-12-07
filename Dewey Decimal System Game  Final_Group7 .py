# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:05:42 2024

@author: izzyg
"""

import random

#  dictoniery and define Dewey Decimal classes and ranges
dewey_classes = {
    "000": "General Works",
    "100": "Philosophy & Psychology",
    "200": "Religion",
    "300": "Social Sciences",
    "400": "Languages",
    "500": "Science",
    "600": "Technology",
    "700": "Arts & Recreation",
    "800": "Literature",
    "900": "History & Geography"
}

#  list and dictonieries and define book titles, descriptions, and categories for Level Two
books = [
    {"title": "Fairy Science", "description": "Esther is a fairy who doesn't believe in magic, so when a forest tree stops growing, she uses the scientific method to discover why.", "answer": "500"},
    {"title": "Ultimate Book of the Future", "description": "Meet space robots, cyborgs, holographic pop stars, and more when you take a peek into how we might live in the future!", "answer": "600"},
    {"title": "Monet's Cat", "description": "When Monet's catstatue comes to life, it jumps into one of Monet's famous paintings! The cat can't be caught as it frolicks and meanders through Monet's greatest works.", "answer": "700"},
    {"title": "Cleopatra Rules!: The Amazing Life of the Original Teen Queen.", "description": "Becoming queen at the age of 17, Cleopatra proved to be an intelligent negotiator and ruler, able to keep herself in power. Read on to learn more about Egypt's last and most famous pharaoh!", "answer": "900"},
    {"title": "Big Ideas for Young Thinkers: 20 Questions About Life and the Universe.", "description": "Explore big ideas from a range of thinkers and decide where you stand on important issues. Questions include: Who am I? What is race? What is justice?", "answer": "100"},
    {"title": "Charlotte's Web", "description": "Charlotte's spiderweb tells of her feelings for a little pig named Wilbur who simply wants a friend, and of Fern, the little girl who saved Wilbur's life.", "answer": "800"},
    {"title": "Library Lion", "description": "When a lion wanders into the library for storytime, he's allowed to stay and help out as long as he follows the rules of the library.", "answer": "000"},
    {"title": "Celebrating Different Beliefs", "description": "No matter what religion people do or don't practice, everyone should have the freedom to practice, and respect each other's religions and practices.", "answer": "200"},
    {"title": "Mariana and Her Familia", "description": "Monica is nervous to go to her Abuelita's party because she doesn't speak Spanish like her Abuelita and other family members. Monica learns there are more ways to communicate, such as cooking and picture books.", "answer": "400"},
    {"title": "How Kids Celebrate Christmas Around the World", "description": "Everyone loves Christmas! But have you ever wondered what Christmas might be like around the world? Learn about different cultures, and how to respect them.", "answer": "300"},
]

# Function for Level One
def play_level_one(score):
    print("\nWelcome to Level One: Match Dewey Decimal Classes!")
    level_one_score = 0

    # Randomize question order
    questions = list(dewey_classes.items())
    random.shuffle(questions)

    for range_, category in questions:
        print(f"\nWhat is the number range for '{category}'?")
        user_answer = input("Enter the correct number range: ").strip()
        if user_answer == range_:
            print("Correct!")
            level_one_score += 1
        else:
            print(f"Wrong! The correct answer is {range_}.")
    
    print(f"\nLevel One Complete! You scored {level_one_score}/{len(dewey_classes)}")
    score += level_one_score * 10  # Each correct answer earns 10 points
    return score

# Function for Level Two
def play_level_two(score):
    print("\nWelcome to Level Two: Match Book Titles to Dewey Decimal Ranges!")
    level_two_score = 0

    # Randomize book order
    random.shuffle(books)

    for book in books:
        print(f"\nBook Title: {book['title']}")
        print(f"Description: {book['description']}")
        user_answer = input("Enter the correct Dewey Decimal range (e.g., 100): ").strip()
        if user_answer == book["answer"]:
            print("Correct!")
            level_two_score += 1
        else:
            print(f"Wrong! The correct anwser is {book['answer']}.")

    print(f"\nLevel Two Complete! You scored {level_two_score}/{len(books)}")
    score += level_two_score * 10  # Each correct answer earns 10 points
    return score

# Main Menu
def main():
    score = 0  # set the score
    print("Welcome to the Dewey Decimal System Game! The Dewey Decimal System is a library classification system that organizes books by subject into 10 main classes (000-900). For example, books on 'Science' fall under the 500s, and books on 'History' fall under the 900s. Let's see how well you know Dewey!")
    print("\nGAME LAYOUT: 1. Level 1: Enter the correct 3-digit class number (000-900) for the provided class name.")
    print("Level 2: Based off of the provided book title and description, enter the correct 3-digit class number the book would fall under.")
    print("3. After Level 1 is complete, you can try again at the same level, or continue to Level 2.")
    print("4. Your scores will be kept! After each level is completed, view them, and try to beat your high score!")

    while True:
        print("\n--- Dewey Decimal Matching Game ---")
        print("1. Play Level One")
        print("2. Play Level Two")
        print("3. Check Score")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            score = play_level_one(score)
        elif choice == "2":
            score = play_level_two(score)
        elif choice == "3":
            print(f"\nYour current score is: {score} points.")
        elif choice == "4":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Wrong choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
