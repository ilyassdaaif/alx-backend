import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));

// Set the value "School" for the key "Holberton"
client.set('Holberton', 'School', redis.print);

// Retrieve the value for the key "Holberton"
client.get('Holberton', (error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log(result);
  }
});

// Close the Redis client connection
client.quit();
