# Use official node image as the base image
FROM node:16 as build

# Set the working directory
WORKDIR /usr/local/app

# Add the source code to app
COPY .. /usr/local/app/

# Run tests
RUN npm install
