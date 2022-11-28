# odoo15
Working on my Odoo cookbook
Odoo 15 Chapter 16 Remote Procedure Calls (RPC)
Calling methods through XML-RPC

Got thrown off by the error msg.  They were caused by the lack of return statements in the methods I called.  Note the last statement of 'return True' that must be added.

    def make_borrowed(self):
        self.ensure_one()
        self.state = 'borrowed'
        return True

Result:
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % python3 
books_method.py
20 (printed out the book id)
Book state after method call: borrowed