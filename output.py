# Create plot figure with context manager 
# Create a plot figure with context manager 
with plt.style.context(('ggplot')): 
    fig, ax = plt.subplots(figsize=(6, 4)) 
    ax.set(title='My Plot', xlabel='x-axis', ylabel='y-axis') 
    ax.plot(x, y) 

# # Create a plot figure with context manager 
with plt.style.context(('fivethirtyeight')): 
    fig, ax = plt.subplots(figsize=(6, 4)) 
    ax.plot(x, y) 
    ax.set(title='My Plot', xlabel='x-axis', ylabel='y-axis') 
