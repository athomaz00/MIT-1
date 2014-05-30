class AccountPounds(AccountDollars):
	def __init__(self, pounds):
		AccountDollars.__init__(self, pounds * 2)

	def depositPounds(self, pounds):
		return self.deposit_dollars(2 * depositPounds)