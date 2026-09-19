# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory

def main():
    print("=== Activity 12: Factory-Driven System Suite ===")

    # TODO (Step 1): Create one account of each type ONLY through AccountFactory.create_account():
    #   "SAVINGS", "CURRENT", "SALARY" and "FIXEDDEPOSIT"
    #   (arguments: account_type, account_number, name, age, balance, status, pin).

    sav = AccountFactory.create_account("SAVINGS", "SAV123", "Alice", 30, 1000.0, "ACTIVE", "1234")
    cur = AccountFactory.create_account("CURRENT", "CUR456", "Bob", 40, 2000.0, "ACTIVE", "5678")
    sal = AccountFactory.create_account("SALARY", "SAL789", "Charlie", 50, 3000.0, "ACTIVE", "9012")
    fix = AccountFactory.create_account("FIXEDDEPOSIT", "FIX321", "David", 60, 4000.0, "ACTIVE", "3456")

    # TODO (Step 2): Using only IAccount members (no concrete class names), assert that each account
    #   balance and get_account_type() match what you created, then exercise deposit()/withdraw().
    assert sav.get_account_type() == "SAVINGS"
    assert sav.balance == 1000.0
    sav.deposit(500.0)
    assert sav.balance == 1500.0
    sav.withdraw(250.0)
    assert sav.balance == 1250.0

    assert cur.get_account_type() == "CURRENT"
    assert cur.balance == 2000.0
    cur.deposit(500.0)
    assert cur.balance == 2500.0
    cur.withdraw(250.0)
    assert cur.balance == 2250.0

    assert sal.get_account_type() == "SALARY"
    assert sal.balance == 3000.0
    sal.deposit(500.0)
    assert sal.balance == 3500.0
    sal.withdraw(250.0)
    assert sal.balance == 3250.0

    assert fix.get_account_type() == "FIXEDDEPOSIT"
    assert fix.balance == 4000.0
    fix.deposit(500.0)
    assert fix.balance == 4500.0
    fix.withdraw(250.0)
    assert fix.balance == 4250.0

if __name__ == "__main__":
    main()
