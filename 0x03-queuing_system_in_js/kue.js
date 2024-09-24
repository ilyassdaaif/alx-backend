import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define a job to be processed
const job = queue.create('email', {
  title: 'welcome email for pablo',
  customer: 'pablo@email.com',
}).save((err) => {
  if (!err) console.log(`Job created: ${job.id}`);
});

// Process the job
queue.process('email', (job, done) => {
  console.log(`Processing job ${job.id}`);
  // Simulate some work
  setTimeout(() => {
    console.log(`Completed job ${job.id}`);
    done();
  }, 2000);
});
