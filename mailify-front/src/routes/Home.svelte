<script lang="ts">
    import FAQ from "../components/home/FAQ.svelte";
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import Hero from "../components/home/Hero.svelte";
    import Features from "../components/home/Features.svelte";
    import HomeBackground from "../components/background/HomeBackground.svelte";

    import { tagline } from "../lib/interfaces/Tagline";
</script>

<div class="flex-col justify-items-center items-center w-full font-helvetica">
    <HomeBackground/>
    <main class="flex-column w-full items-center justify-items-center gap-8">
        <Navbar/>
        <Hero texts={tagline}/>
        <Features/>
        <FAQ/>
        <Footer/>
    </main>
</div>