<script lang="ts">
    import logoDark from '../assets/mailify-dark.png'
    import logoLight from '../assets/mailify-light.png'
</script>

<header class="flex flex-row gap-48 justify-evenly items-center h-36 mx-auto font-helvetica">
    <div class="flex flex-row items-center gap-4">
        <img src={logoLight} class="w-14" alt="logo"/>
        <p class="font-bold text-3xl">Mailify</p>
    </div>

    <div class="items-center">
        <ul class="flex gap-8">
            <a href="#" class="no-underline">Features</a>
            <a href="#" class="no-underline">Privacy Policy</a>
            <a href="#" class="no-underline">Terms of Services</a>
            <a href="#" class="no-underline">Contact Us</a>
        </ul>
    </div>

    <div class="items-center">
        <p class="font-medium text-base font-helvetica
                  border-solid border-2 border-black
                  rounded-2xl py-2 px-4
                  bg-blaze text-midnight">Get Started Free</p>
    </div>
</header>