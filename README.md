# Bitcoin Trace

[![](/report/images/application.png)](https://consto.uk/blockchain-tracer)

This project demonstrates the ability to visualize, and trace transactions through the Bitcoin network, evaluating three different methods. Namely poison, haircut and First-In-First-Out (FIFO).

To achieve this, a web application was created to first build up a network graph representing Bitcoin addresses as nodes, and transactions as directional edges. This allows the user to easily grasp the history of any given Bitcoin address, and then trace any transaction either up or down the graph.

By clicking on a node in the graph, the application will automatically load that address and it's associated transactions, adding it to the graph. By hovering over a node in the graph, the tool-tip on the right will appear. It displays a number of useful statistics about the address, and gives the user the option to trace transactions by clicking on any of the colourful buttons.

* [Try online](https://consto.uk/blockchain-tracer)
* [Read the report](/report.pdf)
