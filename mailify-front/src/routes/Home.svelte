<script lang="ts">
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import HomeBackground from "../components/background/HomeBackground.svelte";
</script>

<div class="flex-col justify-items-center items-center w-full">
    <HomeBackground/>
    <main class="flex-column w-full items-center justify-items-center">
        <Navbar/>

        <div class="flex-column justify-items-center">
            <p class="text-base my-4 font-medium">KNOW EVERY PARAMETER IN EASY REACH</p>
            <p class="text-8xl  my-6 font-semibold">Control Your Car</p>
            <p class="text-8xl  my-6 font-medium">Via Your Phone</p>
        </div>

        <Footer/>
    </main>
</div>