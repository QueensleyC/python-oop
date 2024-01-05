# API Integration and Database Storage

## Overview

This project is designed to demonstrate the integration of external API calls, local database storage, and efficient data retrieval. The primary components include a class responsible for making API calls to fetch data from the internet and an SQL class for storing and retrieving this data in a local database.

## Features

### 1. API Data Fetching

- Utilizes a custom class to make API calls and fetch data from a remote server.
- Provides a flexible and modular design for handling different types of API requests.

### 2. Local Database Storage

- Implements an SQL class that efficiently stores fetched data in a local database.
- Ensures data persistence for offline use and improved performance.

### 3. Data Retrieval

- Includes a method within the SQL class for easy retrieval of stored data.
- Enables seamless integration with other parts of the application that require access to the locally stored data.

## Usage

1. **API Class:**
   - Instantiate the API class and use its methods to make API calls.
   - Handle API responses and extract relevant data for further processing.

2. **SQL Class:**
   - Initialize the SQL class to manage local database interactions.
   - Store fetched data in the database using the provided methods.
   - Retrieve data efficiently using the designated retrieval method.
