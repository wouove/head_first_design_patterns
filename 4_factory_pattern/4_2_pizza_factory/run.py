from pizza_store import NYStylePizzaStore, ChicagoStylePizzaStore

if __name__ == '__main__':
    ny_store = NYStylePizzaStore()
    chicago_store = ChicagoStylePizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.name}")