<script lang="ts">
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import Features from "../components/home/Features.svelte";
    import HomeBackground from "../components/background/HomeBackground.svelte";
    import Hero from "../components/home/Hero.svelte";

    const texts:string[] = [
        "TRANSFORM YOUR EMAILS, UNLOCK OPPORTUNITIES",
        "TRANSFORM YOUR EMAILS, SEIZE NEW POSSIBILITIES",
        "TRANSFORM YOUR EMAILS, OPEN DOORS TO SUCCESS",
        "TRANSFORM YOUR EMAILS, CAPTURE THE ATTENTION YOU DESERVE"
    ]
</script>

<div class="flex-col justify-items-center items-center w-full font-helvetica">
    <HomeBackground/>
    <main class="flex-column w-full items-center justify-items-center gap-8">
        <Navbar/>
        <Hero texts={texts}/>
        <Features/>
        <Footer/>
    </main>
</div>