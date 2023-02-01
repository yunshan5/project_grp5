## import each python file as modules in main.py
import filetouch, cash_on_hand, profit_loss, overheads

## by using methods, execute the functions in their respective modules
## in the filetouch module, use the parameter "summary_report" to name the txt file.
filetouch.create("summary_report.txt")
overheads.overheads_function()
cash_on_hand.coh_function()
profit_loss.pol_function()
