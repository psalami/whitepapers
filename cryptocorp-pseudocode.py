# What would the smart contract code for a crypto corporation look like?
# In this document we can explore some ideas for programming a smart corporation
# that has some level of self-governance and autonomy. It is designed to generate
# maximum positive and growing returns for its investors without the need
# to trust a single individual.

# The examples below are in pseudo-code. The code is written for a fictional
# crypto corporation that provides web development services to its customers.
# It defines shareholders (founders, outside investors), employees, clients,
# vendors and assets.
# It provides for the investment of capital in return for dividends;
# solicitation of clients and employees; generation, execution and approval of tasks;
# addition and removal of members; automatic and semi-automatic management
# and allocation of company assets.


# a real-world entity, such as a vendor or an employee
class Entity(object):
    pass

# any real-world entity that is involved in the corporation
# (let's assume that all employees and shareholders are considered members)
class Member(Entity):
    pass

# a real-world entity that has an interest in the corporation
class Shareholder(Member):
    pass

# a real-world entity (let's assume a natural person) who has the ability
# to perform Tasks on behalf of the corporation
class Employee(Employee):
    pass

# a real-world entity (let's assume a natural person) who
# has certain decision-making privileges not available to other
# Employees
class Director(Employee):
    pass

# a real-world entity (may be another corporation) that may trade an Asset
# for a Liability
class Client(Entity):
    pass

# a real-world entity (may be another corporation) that may trade a Liability
# for an Asset
class Vendor(Entity):
    pass

# a real-world asset (may be a physical asset like real estate, or work that
# was done by an Employee on behalf of the corporation)
class Asset(object):
    creation_date #the date on which the Asset was created or acquired
    liquidation_date #the date on which the Asset was disposed of
    value #cash value of this asset (assume values are in digital currency)

# a real-world liability (i.e. work that is to be done by an employee for a
# Client or an invoice that is to be paid to a Vendor)
class Liability(object):
    creation_date #the date on which the Liability was created
    liquidation_date #the date on which the Liability was settled
    value #cash value of this asset (assume values are in digital currency)
    const_type #one of i.e.: wage, tax, operating_expense
    due_date #to differentiate, i.e. between long-term, short-term liabilities
    bool_contingent #true or false; whether or not this is a contingent liability

# a real-world service that the corporation can sell to a Client
class Sellable(object):
    pass


class Account(object):
    assets[]
    liabilities[]
    cash_balance


class AssetManager(object):

    def net_income(start_date, end_date):
        net_income = 0
        for account in Corporation.accounts:
            for asset in account.assets:
                if asset.creation_date >= start_date and asset.creation_date <= end_date:
                    net_income += asset.value
            for liability in account.liabilities:
                if liability.creation_date >= creation_date and liability.creation_date <= end_date:
                    net_income -= liability.value
        return net_income


class CapTable(object):
    #a hash table mapping shareholder addresses
    #to their respective share positions
    shareholder_positions = {}
    #records of all share purchases or sales
    transactions[]

#represents a real-world purchase or sale of shares between the corporation
#and an Entity (i.e. a shareholder)
class ShareTransaction(object):
    transaction_date
    value
    num_shares #for share transactions
    shareholder


class Corporation(object):

    #can be changed only by i.e. a majority shareholder vote
    earnings_multiple = 5
    #total number of shares issued by the corporation; can be increased only by
    #i.e. a majority shareholder vote
    num_shares = 1000000
    #all accounts held by this corporation
    accounts[]

    # compute a price per share at which to offer equity to new investors;
    # a more complex way of computing the share price can be implemented
    # here; the algorithm to compute the price should not change over time, however
    # the constants (i.e. earnings_multiple) can be adjusted, i.e. by a majority
    # vote of shareholders
    def get_price_per_share():
        return AssetManager.net_income(today - 1yr, today) / self.num_shares
                    * self.earnings_multiple

    def get_owners_equity():
        owners_equity = 0
        for account in self.accounts:
            for asset in account.assets:
                owners_equity += asset.value
            for liability in account.liabilities:
                owners_equity -= liability.value
        return owners_equity

    # this public method allows the calling client / wallet to obtain
    # a profits interest (or equity stake) in this Corporation
    #
    # shareholder - the address of the client / wallet calling this method
    # num_shares - the number of shares to be purchased
    # input_transaction - the transaction containing the consideration for the shares
    def buy_shares(shareholder, num_shares, input_transaction):
        if input_transaction.value < num_shares * self.get_price_per_share():
            return False
