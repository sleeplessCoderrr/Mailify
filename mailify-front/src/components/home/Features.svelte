<script lang="ts">
    import { features } from "../../lib/interfaces/Features";
</script>

<div class="w-4/6 mt-48 mb-24 flex flex-col justify-items-center align-middle text-center gap-12">
    <div>
        <p class="font-bold text-4xl mb-4">Why Choose Mailify?</p>
        <p class="text-lg">Highlight the core benefits and functionality of Mailify.</p>
    </div>
    <div class="grid grid-cols-3 gap-8">
        {#each features as feature}
            <div class="bg-mist/40 backdrop-blur-sm shadow-lg border-2 border-stone-300 rounded-md p-8 text-center">
                <i class="{feature.icon} text-4xl animate-bounce mb-4 text-blaze/80"></i>
                <h3 class="text-xl font-bold text-primary mb-4">
                    {feature.title}
                </h3>
                <p class="text-midnight">
                    {feature.description}
                </p>
            </div>
        {/each}
    </div>
</div>