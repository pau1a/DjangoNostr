# Djangstr

# A Django Nostr Relay

This is a Django project that has been modified to accept WebSocket connections and acts as a Nostr relay. The Nostr relay allows real-time communication between clients and servers using the WebSocket protocol.

## Features

- WebSocket support: The project has been integrated with Django Channels to handle WebSocket connections.
- Nostr relay functionality: It acts as a relay server for Nostr, a real-time messaging protocol.
- Authentication and Authorization: Users can authenticate and authorize their WebSocket connections using Django's built-in authentication system.
- Real-time messaging: Clients can send and receive real-time messages through the relay server.

## Installation

1. Clone the repository:

```
git clone https://github.com/pau1a/Djangstr.git
```

2. Change to the project directory:

```
cd Djangstr
```

3. Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

4. Install the project dependencies:

```
pip install -r requirements.txt
```

5. Set up the database:

```
python manage.py migrate
```

## Configuration

1. Rename the `.env.example` file to `.env`:

```
mv .env.example .env
```

2. Edit the `.env` file and update the following settings:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost
```

3. Generate a new secret key and replace `your_secret_key` with the generated key.

## Usage

1. Start the development server:

```
python manage.py runserver
```

2. Open your web browser and visit `http://localhost:8000`.

3. To access the WebSocket functionality, connect to `ws://localhost:8000/ws/`.

4. Authenticate and authorize WebSocket connections using the available API endpoints (e.g., `/api/auth/login/`).

## API Endpoints

The project provides the following API endpoints for authentication and WebSocket connection management:

- `POST /api/auth/login/`: Authenticate a user and retrieve an authentication token.
- `POST /api/auth/logout/`: Log out the currently authenticated user.
- `GET /api/auth/user/`: Retrieve information about the currently authenticated user.
- `GET /api/ws/connect/`: Establish a WebSocket connection.
- `GET /api/ws/disconnect/`: Close a WebSocket connection.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

Please ensure that your code follows the project's coding style and is accompanied by unit tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to reach out to the project maintainer at [p a u l a @paulalivingstone.com](mailto:p a u l a @paulalivingstone.com).
