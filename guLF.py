#!/usr/bin/env python
import ConfigParser
import os
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        self.configPath = os.environ['APPDATA'] + '\\Logic Friday\\gate-sizes.ini' 
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.configPath)
        self.gates = ['Inverter',
                     '2-In NAND', '3-In NAND', '4-In NAND',
                     '2-In NOR', '3-In NOR', '4-In NOR',
                     '2-In XOR',
                     '2-In MUX',
                     '2-In AND', '3-In AND', '4-In AND',
                     '2-In OR', '3-In OR', '4-In OR']
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.NSEW, padx=5, pady=5)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        lbl = tk.Label(self, text='Size')
        lbl.grid(row=0, column=1)
        self.entries = []
        i=1
        validateEntryCommand = self.register(self.validateEntry)
        for gate in self.gates:
            self.rowconfigure(i, weight=1)
            lbl = tk.Label(self, text=gate+':')
            lbl.grid(row=i, sticky=tk.E)
            e = tk.Entry(self, width=10,
                         validate='all', validatecommand=(validateEntryCommand, '%P'))
            iniLabel = gate.replace(' ', '_')
            if self.config.has_option('Gate Sizes', iniLabel):
                value = self.config.getfloat('Gate Sizes', iniLabel)
            else:
                value = 0
            # ignore decimal places that are zero
            value = "%g"%value
            e.insert(0, value)
            e.grid(row=i, column=1, sticky=tk.EW, padx=10, pady=5)
            self.entries.append(e)
            i=i+1

        frame = tk.Frame()
        frame.grid(row=i, column=0, columnspan=2)
        self.saveBtn = tk.Button(frame, text='OK', width=10,
                              command = self.save)
        self.saveBtn.grid(row=0, column=0, pady=10, padx=5)
        cancelBtn = tk.Button(frame, text='Cancel', width=10,
                           command = self.quit)
        cancelBtn.grid(row=0, column=1, pady=10, padx=5)

    def validateEntry(self, newValue):
        if newValue == "":
            return True
        try:
            float(newValue)
            return True
        except:
            return False

    def save(self):
        # don't use ConfigParser to retain order of keys
        with open(self.configPath, 'w') as f:
            f.write('[Gate Sizes]\n')
            for i in range(len(self.entries)):
                label = self.gates[i].replace(' ', '_')
                value = self.entries[i].get()
                if value == "":
                    value = "0"
                f.write('%s = %s\n'%(label, value))
        self.quit()
 
app = Application()
app.master.title('guLF')
app.mainloop()
