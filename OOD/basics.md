## Object Oriented Design

# Step 1: Handle Ambiguity
- Often intentionally vague to test whether you'll make assumptions or you'll ask questions
- asking questions are better

ask
- WHO is going to use it?
- HOW are they going to use it?
- Depending on the question, six Ws

# Step 2: Define the Core Objects

For example.. design a restaurant.

Our core objects might be things like
Table, Party, Order, Guest, Server, Customer, Host

# Step 3: Analyze Relationships

- which objects are members of which other objects?
- do any objects inherit from any others?
- are relationships many-to-many or one-to-many?

ex) 
- Party should have an array of Guests
- Server and Host inherit from Employee
- Each Table has 1 party, but each party have multiple Tables
- There is one Host for the Restaurant

# Step 4: Investigate Actions

- Consider key actions that each object can take and how they relate to each other

ex)
- Party 'walks into the' Restaurant
- Guest 'requests' a Table from the Host
- Host 'looks up' the Reservation
- if it exists, assigns the Party to a Table
- otherwise, Party is added to the end of the Reservation list
- When a Party leaves, the Table is freed and assigned to a new Party in the list

# Singleton Class vs Factory Method

- Singleton Class: having one instance that ensures access to all of the application's features
ex) one Restaurant Class

class Restaurant:
    def __init__(self):
        self.instance = None
    def getInstance(self):
        if not self.instance:
            self.instance = new Restaurant()

- Factory Method: The Factory Method offers an interface for creating an instance of a class,
with its subclasses deciding which class to instantiate

public class CardGame {
    public static CardGame createCardGame(GameType type) {
        if (type == GameType.Poker){
            return new PokerGame()
        } else if (type == GameType.BlackJack) {
            return new BlackJackGame()
        }
    }
}