import { useEffect, useState } from 'react';

export default function Home() {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/listings/')
      .then(res => res.json())
      .then(data => setListings(data));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Airbnb Listings</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {listings.map((listing, idx) => (
          <div key={idx} className="bg-white p-4 rounded-xl shadow-md">
            <img src={listing.image_urls[0]} className="w-full h-40 object-cover rounded-md" />
            <h2 className="text-xl font-semibold mt-2">{listing.title}</h2>
            <p>{listing.location}</p>
            <p>${listing.price_per_night}/night</p>
            <p>⭐ {listing.ratings} ({listing.num_reviews} reviews)</p>
          </div>
        ))}
      </div>
    </div>
  );
}
