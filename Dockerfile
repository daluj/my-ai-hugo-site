# Use Hugo extended version with Alpine
FROM klakegg/hugo:ext-alpine AS builder

WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN apk add --no-cache nodejs npm && \
    npm install -g postcss-cli autoprefixer tailwindcss

# Build TailwindCSS
RUN npm run build:css

# Build the Hugo site
RUN hugo --minify

# Final production image
FROM nginx:alpine

# Copy generated site from the builder stage
COPY --from=builder /app/public /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]