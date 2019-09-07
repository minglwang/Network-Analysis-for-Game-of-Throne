# -*- coding: utf-8 -*-
# =============================================================================
# # Importing modules
# =============================================================================
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
#import nxviz as nv
# Reading in datasets/book1.csv
book1 = pd.read_csv("datasets/book1.csv")

# Printing out the head of the dataset
print(book1.head())

# Importing modules

# Creating an empty graph object
G_book1 = nx.Graph()


# Iterating through the DataFrame to add edges
# After add those edges, the nodes are contained in the Graph
for index, edge in book1.iterrows():
    G_book1.add_edge(edge['Source'], edge['Target'],  weight = edge['weight'])

# =============================================================================
# Plot the graph and show the 5 most important nodes
# =============================================================================
# find the node of interest with top betweeness_centrality

def graph_view(G,num = 5):
    bw_cen = nx.betweenness_centrality(G)
    top_bw_cen = sorted(bw_cen.values(), reverse = True)[:num]
    noi = [n for n in G.nodes() if bw_cen[n] in top_bw_cen]
    node_color = [bw_cen[n] for n in G.nodes()]
    edge_width = [d['weight']/30 for u, v, d in G.edges(data = True)]
    # node_size is propotional to its connectivity i.e. number of edges
    node_size =  [10*len(G.edges(n)) for n in G.nodes()]
    pos=nx.spring_layout(G)
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos ,node_color = node_color, edge_color='k', width =edge_width  ,node_size = node_size,with_labels=False)
    #for p in noi:  # raise text positions
    #    pos[p][1] += 0.07
    
    # Only plot the node of interest
    pos_noi = {n : pos[n] for n in noi}
    nx.draw_networkx_labels(G.subgraph(nodes = noi), pos_noi,font_size = '15', \
                            font_weight='bold' ,font_color = 'r')
    plt.title('Graph Model of GameOfThrone')
    plt.show()




# Creating a list of networks for all the books
books = [G_book1]
book_fnames = ['datasets/book2.csv', 'datasets/book3.csv', 'datasets/book4.csv', 'datasets/book5.csv']
for book_fname in book_fnames:
    book = pd.read_csv(book_fname)
    G_book = nx.Graph()
    for _, edge in book.iterrows():
        G_book.add_edge(edge['Source'], edge['Target'], weight=edge['weight'])
    books.append(G_book)


# =============================================================================
# plot all the books
# =============================================================================
book = books[3]
for book in books:
    graph_view(book, 5)


# Calculating the degree centrality of book 1
deg_cen_book1 = nx.degree_centrality(books[0])

# Calculating the degree centrality of book 5
deg_cen_book5 = nx.degree_centrality(books[4])


# =============================================================================
# # Sorting the dictionaries according to their degree centrality and storing the top 10
# =============================================================================
sorted_deg_cen_book1 = sorted(deg_cen_book1.items(), key = lambda x:x[1], reverse = True )

# Sorting the dictionaries according to their degree centrality and storing the top 10
sorted_deg_cen_book5 =  sorted(deg_cen_book5.items(), key = lambda x:x[1], reverse = True)

# Printing out the top 10 of book1 and book5
print(sorted_deg_cen_book1[:10])
print(sorted_deg_cen_book5[:10])

# =============================================================================
# Graph change overtime
# =============================================================================
# Instantiate a list of graphs that show edges added: added
added_nodes = []
added_edges = []
# Instantiate a list of graphs that show edges removed: removed
removed_nodes = []
removed_edges = []

# Here's the fractional change over time
fractional_changes = []
window = 1  
i = 0 
for i in range(len(books) - window):
    
    g1 = books[i]
    g2 = books[i + window]
        
    # Compute graph difference here
    # nx.difference Parameters:	
    #  G,H (graph) – A NetworkX graph. G and H must have the same node sets.
#    added.append(nx.difference(g2,g1))   
#    removed.append(nx.difference(g1,g2))
    added_nodes.append(g2.nodes()-g1.nodes()) 
    removed_nodes.append(g1.nodes()-g2.nodes())
    added_edges.append(g2.edges()-g1.edges()) 
    removed_edges.append(g1.edges()-g2.edges())
    # Compute change in graph size over time
    fractional_changes.append((len(g2.edges()) - len(g1.edges())) / len(g1.edges()))
    
# Print the fractional change
print(fractional_changes)

# =============================================================================
# Plot the change overtime
# =============================================================================
fig = plt.figure(figsize = (8,4))
plt.title('change over time book1--book4')
ax1 = fig.add_subplot(111)

# Plot the number of edges added over time
edges_added = [len(edges) for edges in added_edges]
plot1 = ax1.plot(edges_added, label='added edges', color='orange')

# Plot the number of edges removed over time
edges_removed = [len(edges) for edges in removed_edges]
plot2 = ax1.plot(edges_removed, label='removed edges', color='purple')

# Set yscale to logarithmic scale
ax1.set_yscale('log')  
ax1.legend()

# 2nd axes shares x-axis with 1st axes object
ax2 = ax1.twinx()

# Plot the fractional changes over time
plot3 = ax2.plot(fractional_changes, label='fractional change', color='green')

# Here, we create a single legend for both plots
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc=0)
plt.axhline(0, color='green', linestyle='--')
plt.show()
#%matplotlib inline

# Creating a list of degree centrality of all the books
evol = [nx.degree_centrality(book) for book in books]
 
# Creating a DataFrame from the list of degree centralities in all the books
degree_evol_df = pd.DataFrame.from_records(evol) # convenient to work with pandas

# Plotting the degree centrality evolution of Eddard-Stark, Tyrion-Lannister and Jon-Snow
degree_evol_df[['Eddard-Stark', 'Tyrion-Lannister', 'Jon-Snow']].plot(title = 'evolution of degree of centrality')

# Creating a list of betweenness centrality of all the books just like we did for degree centrality
evol = [nx.betweenness_centrality(book) for book in books]

# Making a DataFrame from the list
betweenness_evol_df = pd.DataFrame.from_records(evol).fillna(0)


# =============================================================================
# # Finding the top 4 characters in every book
# =============================================================================
set_of_char = set()
for i in range(5):
    set_of_char = set(list(betweenness_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)

# =============================================================================
# # Plotting the evolution of the top characters
# =============================================================================

betweenness_evol_df[list_of_char].plot(figsize=(13, 7), title = 'Top 4 characters')

# Creating a list of pagerank of all the characters in all the books
evol = [nx.pagerank(book) for book in books ]

# Making a DataFrame from the list
pagerank_evol_df = pd.DataFrame.from_records(evol)

# =============================================================================
# # Finding the top 4 characters in every book
# =============================================================================
# |= Adds elements from another set

set_of_char = set()
for i in range(5):
    set_of_char |= set(list(pagerank_evol_df.T[i].sort_values(ascending=False)[0:4].index))
    print(set_of_char)

list_of_char = list(set_of_char)

# =============================================================================
# # Plotting the top characters
# =============================================================================
pagerank_evol_df[list_of_char].plot(figsize=(13, 7), title = 'page rank evoluation along book1 to book4')
# Creating a list of pagerank, betweenness centrality, degree centrality
# of all the characters in the fifth book.
measures = [nx.pagerank(books[4]), 
            nx.betweenness_centrality(books[4], weight='weight'), 
            nx.degree_centrality(books[4])]

# Creating the correlation DataFrame
cor = pd.DataFrame.from_records(measures)
print(cor.head())
# Calculating the correlation
cor.T.corr()

# =============================================================================
# # Finding the most important character in the fifth book,  
# # according to degree centrality, betweenness centrality and pagerank.
# =============================================================================
p_rank, b_cent, d_cent =  cor.idxmax(axis=1)

# Printing out the top character accoding to the three measures
print(p_rank)
print(b_cent)
print(d_cent)

