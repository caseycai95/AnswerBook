# Define variables
APP_NAME = answerbook
HOST = 0.0.0.0
PORT = 8080

# Command to start the API
start:
	@echo "Starting $(APP_NAME) API..."
	uvicorn main:app --host $(HOST) --port $(PORT)

# Command to stop (optional, if using a background process manager like pm2)
stop:
	@echo "Stopping $(APP_NAME) API..."
	# Add stop command here if needed

# Command to run tests (optional)
test:
	@echo "Running tests..."
	# Add test command here if needed

# Command to build Docker image (optional)
build:
	@echo "Building Docker image for $(APP_NAME)..."
	docker build -t $(APP_NAME)-app .

# Command to clean up (optional)
clean:
	@echo "Cleaning up..."
	# Add clean-up commands here if needed