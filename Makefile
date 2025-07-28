# ROV Skin Sorter Makefile

.PHONY: dev build start lint clean sort-ids help

# Development commands
dev:
	@echo "Starting development server..."
	yarn dev

build:
	@echo "Building for production..."
	yarn build

start:
	@echo "Starting production server..."
	yarn start

lint:
	@echo "Running linter..."
	yarn lint

# Utility commands
clean:
	@echo "Cleaning node_modules and build files..."
	rm -rf node_modules
	rm -rf .nuxt
	rm -rf dist

install:
	@echo "Installing dependencies..."
	yarn install

# Sort ROV skin IDs sequentially
sort-ids:
	@echo "Sorting ROV skin IDs sequentially..."
	@awk ' \
		BEGIN { counter = 1 } \
		/^[[:space:]]*id: [0-9]+,/ { \
			gsub(/id: [0-9]+,/, "id: " counter ","); \
			counter++ \
		} \
		{ print } \
	' lib/skin.ts > lib/skin_temp.ts && mv lib/skin_temp.ts lib/skin.ts
	@echo "ROV skin IDs have been sorted sequentially (1-$$(grep -c 'id: [0-9]*,' lib/skin.ts))"

# Verify ID sorting
verify-ids:
	@echo "Verifying ID sorting..."
	@echo "First 10 IDs:"
	@grep "id: [0-9]*," lib/skin.ts | head -10
	@echo "Last 10 IDs:"
	@grep "id: [0-9]*," lib/skin.ts | tail -10
	@echo "Total IDs: $$(grep -c 'id: [0-9]*,' lib/skin.ts)"

# Show help
help:
	@echo "ROV Skin Sorter - Available commands:"
	@echo ""
	@echo "Development:"
	@echo "  make dev       - Start development server (port 8000)"
	@echo "  make build     - Build for production"
	@echo "  make start     - Start production server"
	@echo "  make lint      - Run linter"
	@echo ""
	@echo "Utilities:"
	@echo "  make install   - Install dependencies"
	@echo "  make clean     - Clean node_modules and build files"
	@echo "  make sort-ids  - Sort ROV skin IDs sequentially"
	@echo "  make verify-ids - Verify ID sorting"
	@echo "  make help      - Show this help message"

# Default target
all: install dev