import express from 'express';
import redis from 'redis';
import kue from 'kue';

// Create an Express app
const app = express();

// Create a Redis client
const client = redis.createClient();

// Create a Kue queue
const queue = kue.createQueue();

// Middleware to parse JSON requests
app.use(express.json());

// Route to set a value in Redis
app.post('/set', (req, res) => {
  const { key, value } = req.body;
  client.set(key, value, redis.print);
  res.send(`Set ${key} to ${value}`);
});

// Route to get a value from Redis
app.get('/get/:key', (req, res) => {
  const { key } = req.params;
  client.get(key, (error, result) => {
    if (error) {
      console.error(error);
      res.status(500).send('Error getting value');
    } else {
      res.send(result);
    }
  });
});

// Route to add a job to the Kue queue
app.post('/jobs', (req, res) => {
  const job = queue.create('email', req.body).save((err) => {
    if (!err) {
      console.log(`Job created: ${job.id}`);
      res.json({ jobId: job.id });
    } else {
      res.status(500).send('Error creating job');
    }
  });
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
