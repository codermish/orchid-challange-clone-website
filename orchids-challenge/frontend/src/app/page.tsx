'use client';

import { useState } from 'react';

export default function Home() {
  const [inputUrl, setInputUrl] = useState('');
  const [clonedHTML, setClonedHTML] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchClonedHTML = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await fetch('http://127.0.0.1:8000/clone', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: inputUrl }),
      });

      if (!res.ok) {
        throw new Error('Failed to clone website');
      }

      const data = await res.json();
      setClonedHTML(data.html);
    } catch (err: any) {
      setError(err.message || 'Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-10 bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">🌐 Website Cloner</h1>

      <div className="max-w-xl mb-4">
        <input
          type="text"
          value={inputUrl}
          onChange={(e) => setInputUrl(e.target.value)}
          placeholder="Enter a public website URL (e.g., https://example.com)"
          className="border border-gray-300 rounded px-4 py-2 w-full"
        />
      </div>

      <button
        onClick={fetchClonedHTML}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        disabled={!inputUrl || loading}
      >
        {loading ? 'Cloning...' : 'Clone Website'}
      </button>

      {error && <p className="text-red-600 mt-4">{error}</p>}

      <div className="mt-8">
        <h2 className="text-xl font-semibold mb-2">🔁 Cloned HTML Preview:</h2>
        <div
          className="bg-white border rounded p-4"
          dangerouslySetInnerHTML={{ __html: clonedHTML }}
        />
      </div>
    </main>
  );
}
