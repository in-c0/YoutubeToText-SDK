import fetch from 'node-fetch';

async function getTranscript(videoID, apiKey, lang) {
  const url = new URL(`https://api.youtubetotext.com/transcript/${videoID}`);
  if (lang) url.searchParams.set('lang', lang);

  const res = await fetch(url, {
    headers: { 'Authorization': `Bearer ${apiKey}` },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const json = await res.json();
  console.log(json.segments.map(seg => seg.text).join("\n"));
}

getTranscript("qT6hMn8vFZo", "YOUR_API_KEY", "en").catch(console.error);
