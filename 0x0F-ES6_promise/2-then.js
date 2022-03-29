export default function handleResponseFromAPI(promise) {
  const body = { status: 200, body: 'success' };
  const response = 'Got a response from the API';
  return promise
    .then(() => body)
    .catch((error) => error)
    .finally(() => console.log(response));
}
