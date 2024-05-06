# Use the official Python image from Docker Hub
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Expose the port on which your Streamlit app will run
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
