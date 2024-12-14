<script lang="ts">
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import HomeBackground from "../components/background/HomeBackground.svelte";
</script>

<div class="flex-col justify-items-center items-center w-full">
    <HomeBackground/>
    <main class="flex-column w-full items-center justify-items-center">
        <Navbar/>

        <div class="flex-column">
            <p>KNOW EVERY PARAMETER IN EASY REACH</p>
            <h1>Control Your Car Via Your Phone</h1>
        </div>

        <Footer/>
    </main>
</div>