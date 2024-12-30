<script lang="ts">
    import { features } from "../../lib/interfaces/Features";
</script>

<div class="w-3/4 mt-36 flex justify-between gap-8">
    {#each features as feature}
        <div class="bg-mist/40 backdrop-blur-sm shadow-lg border-2 border-stone-300 rounded-md p-8 text-center">
            <div class="text-4xl animate-bounce mb-4">
                {feature.emoji}
            </div>
            <h3 class="text-xl font-bold text-primary mb-4">
                {feature.title}
            </h3>
            <p class="text-gray-600">
                {feature.description}
            </p>
        </div>
    {/each}
</div>